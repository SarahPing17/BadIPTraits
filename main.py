#!/usr/bin/env python3
import database

def main():
    print("test")
    db = database.DataBase()
    
    db.getIPs(file_path="opendbl_etknown.txt")


if __name__ == "__main__":
    main()