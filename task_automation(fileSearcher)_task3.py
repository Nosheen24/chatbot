import os
import datetime
import argparse
from progress.bar import Bar


class FileSearch:
    def __init__(self):
        self.file_count = 0
        self.progress_bar = Bar('Searching', suffix='%(eta)ds')

    def get_file_count(self, path, is_folder):

        if not is_folder:
            print("[INFO] Reading files ...")
        else:
            print("[INFO] Reading folders ...")

        self.file_count = 0
        for root, dirs, files in os.walk(path):
            if is_folder:
                self.file_count += len(dirs)
            else:
                self.file_count += len(files)

    def __perform_search(
        self,
        search_term,
        start_dir,
        is_folder,
        disable_case,
        show_bar
    ):
        results = []
        for root, dirs, files in os.walk(start_dir):
            if is_folder:
                for dir in dirs:

                    if show_bar:
                        self.progress_bar.next()

                    if disable_case and search_term in dir:
                        results.append(os.path.join(root, dir))
                    elif not disable_case and search_term.lower() in dir.lower():
                        results.append(os.path.join(root, dir))
            else:
                for file in files:

                    if show_bar:
                        self.progress_bar.next()

                    if disable_case and search_term in file:
                        results.append(os.path.join(root, file))
                    elif not disable_case and search_term.lower() in file.lower():
                        results.append(os.path.join(root, file))

        return results

    def search(
        self,
        search_term,
        start_dir,
        is_folder=False,
        disable_case=False,
        show_bar=True
    ):
        self.file_count = 0
        self.get_file_count(start_dir, is_folder)
        self.progress_bar.max = self.file_count

        if not os.path.exists(start_dir):
            raise Exception(f"Path {start_dir} does not exist.")

        start_time = datetime.datetime.now()
        result = self.__perform_search(
            search_term,
            start_dir,
            is_folder,
            disable_case,
            show_bar
        )
        end_time = datetime.datetime.now()

        if not is_folder:
            print(
                f"\n\n[INFO] Searched {self.file_count:,} files in {(end_time-start_time).total_seconds()} seconds")
        else:
            print(
                f"\n\n[INFO] Searched {self.file_count:,} folders in {(end_time-start_time).total_seconds()} seconds")

        return result


if __name__ == "__main__":

    search_term = input("Enter the search term: ")
    start_dir = input("Enter the directory to search in: ")

    x=input("Search item is folder or file? yes/no :")
    if(x=='no'or x=='yes'):
        is_folder = True
    else:
        is_folder=False
    disable_case = True

    show_bar = True

    searcher = FileSearch()
    results = searcher.search(
        search_term,
        start_dir,
        is_folder,
        disable_case,
        show_bar
    )

    print("[INFO] Results: \n")
    for path in results:
        print("Path:", path)
    print("")
