# import pymongo
# client = pymongo.MongoClient...

from pymongo import MongoClient
from bson import ObjectId
# pymongo does not convert str into json directly so we import objectid from bson

client = MongoClient("mongodb+srv://pythontutorial:pythontutorial@pythontutorial.hndobwl.mongodb.net/ytmanager")
# not a good practice to include id and password in the codebase
# good practice: keep them in .env or .gitignore files

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def update_video(new_name, new_time, video_id):
    video_collection.update_one(
        {'_id': ObjectId(video_id)}, 
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})



def main():
    while True:
        print("\nYoutube Manager App")
        print("1. List all videos")
        print("2. Add new video(s)")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit app")
        choice = input("Enter the index number: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video id to update: ")
            new_name = input("Enter the updated name for video: ")
            new_time = input("Enter the updated time for video: ")
            update_video(new_name, new_time, video_id)
        elif choice == "4":
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid index choice!")

if __name__ == "__main__":
    main()