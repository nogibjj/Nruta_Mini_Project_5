from mylib.extract import extract
from mylib.query import query
from mylib.transform_load import load


def main():
    # extracting data
    file_path = extract()

    # loading data into database
    load(file_path)

    # performing CRUD operations
    # Create a new biopic record
    query.create_biopic(
        "Back to Black",
        "New Site",
        "United Kingdom",
        2024,
        "$50.8",
        "Sam Taylor-Johnson",
    )

    # Read and display all biopic records
    biopics = query.read_biopics()
    print("All Biopics:")
    for biopic in biopics:
        print(biopic)

    # Display updated list of biopics
    updated_biopics = query.read_biopics()
    print("\nUpdated Biopics after Insertion:")
    for biopic in updated_biopics:
        print(biopic)

    # Assuming you want to update and delete an existing biopic:
    # Get the first biopic ID for demonstration (make sure at least one record exists)
    if updated_biopics:
        biopic_id = updated_biopics[0][
            0
        ]  # This assumes the ID is the first column in the fetched results
        print(f"\nUpdating Biopic ID: {biopic_id}")
        query.update_biopic(
            biopic_id,
            "Updated Biopic Title",
            "Updated Site",
            "Updated Country",
            2024,
            "2000000",
            "Updated Director",
        )

        # Delete the newly created biopic record (assuming you want to delete the last entry)
        print(
            f"\nDeleting Biopic ID: {updated_biopics[-1][0]}"
        )  # Deletes the last biopic
        query.delete_biopic(updated_biopics[-1][0])

    # Final read to verify changes
    final_biopics = query.read_biopics()
    print("\nFinal Biopics after Update and Delete:")
    for biopic in final_biopics:
        print(biopic)


if __name__ == "__main__":
    main()
