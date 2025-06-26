import os
import sys
from pymongo import UpdateOne, ASCENDING, errors
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.singleton import Singleton


class InsertData(metaclass=Singleton):
    """
    This code is used to push data in db. Insert/Upsert records based on unique keys.
    """

    @staticmethod
    def unique_keys():
        return {
            "Jobs": ["job_id"],
            "People": ["username"],
            "Posts": ["postUrl"],
            "Company": ["companyId"],
            "RawJobs": ["job_id"],
            "RawPeople": ["username"],
            "RawPosts": ["postUrl"],
            "RawCompany": ["companyId"],
            "FinalData": ["profileURL"],
            "Query": ["query_id"],
        }

    @staticmethod
    def prepare_data(df):
        """Adds a UTC timestamp to each record in the DataFrame."""
        data_dict = df.to_dict(orient="records")
        current_timestamp = datetime.utcnow().isoformat()
        for record in data_dict:
            record["message_date"] = current_timestamp
        return data_dict

    def ensure_indexes(self, client):
        """Create indexes for collections based on unique keys to ensure efficient upserts."""
        for collection_name, keys in self.unique_keys().items():
            collection = client.get_collection(collection_name)
            try:
                collection.create_index(
                    [(key, ASCENDING) for key in keys], unique=True, background=True
                )
                print(f"Ensured index on {collection_name} for keys: {keys}")
            except Exception as e:
                print(f"Failed to create index on {collection_name}: {e}")

    def insert_or_upsert_to_mongo(self, client, collection_name, data):
        """Insert or upsert records into a MongoDB collection based on unique key constraints."""
        if not data:
            print(f"No data to insert for {collection_name}.")
            return

        unique_keys = self.unique_keys().get(collection_name)
        if not unique_keys:
            raise ValueError(
                f"No unique key defined for collection '{collection_name}'"
            )

        collection = client.get_collection(collection_name)

        operations = []
        skipped = 0

        for record in data:
            filter_criteria = {
                key: record.get(key) for key in unique_keys if key in record
            }
            if len(filter_criteria) != len(unique_keys):
                skipped += 1
                continue  # Skip if any unique key is missing in this record

            operations.append(UpdateOne(filter_criteria, {"$set": record}, upsert=True))

        if not operations:
            print(
                f"No valid records to upsert for {collection_name}. Skipped {skipped} records."
            )
            return

        try:
            result = collection.bulk_write(operations, ordered=False)
            print(
                f"{collection_name} - Upserts: {len(result.upserted_ids)}, Updates: {result.modified_count}, Skipped: {skipped}"
            )
        except errors.BulkWriteError as bwe:
            print(f"Bulk write error in {collection_name}: {bwe.details}")
        except Exception as e:
            print(f"Failed to insert/upsert data into {collection_name}: {e}")
