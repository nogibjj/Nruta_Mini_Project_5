from mylib.extract import extract
from mylib.query import (
    create_biopic,
    read_biopics,
    update_biopic,
    delete_biopic,
)
from mylib.transform_load import load


def main():
    # extracting data
    file_path = extract()

    # loading data into database
    load(file_path)

    # performing CRUD operations
    # Create a new biopic record
    create_biopic(
        "Biopics",
        "Back to Black",
        "https://www.imdb.com/title/tt21261712/",
        "United Kingdom",
        2024,
        "$50.8",
        "Sam Taylor-Johnson",
        1,
        "Amy Winehouse",
        "Musician",
        "Yes",
        "White",
        "No",
        "Female",
        "Marisa Abela",
    )

    # Read and display all biopic records
    biopics = read_biopics("Biopics")
    print("All Biopics:")
    for biopic in biopics:
        print(biopic)

    # Display updated list of biopics
    updated_biopics = read_biopics("Biopics")
    print("\nUpdated Biopics after Insertion:")
    for biopic in updated_biopics:
        print(biopic)

    print("\nUpdating the Back to Black biopic...")
    update_biopic(
        "Biopics",
        "Updated Biopic Title",
        "Updated Site",
        "Updated Country",
        2024,
        "Updated box office",
        "Updated Director",
        "Updated no. of subjects",
        "Updated Subject",
        "Updated Type of Subject",
        "Updated Race Known",
        "Updated Subject Race",
        "Updated Person of Color",
        "Updated Subject Sex",
        "Updated Lead Actor/Actress",
    )

    updated_biopics = read_biopics("Biopics")
    print("\nUpdated biopics after insertion and update:")
    for biopic in updated_biopics():
        print(biopic)

    print("\nDeleting Back to Black biopic...")
    delete_biopic("biopics.db", "Back to Black")

    # final read to verify changes
    final_biopics = read_biopics("Biopics")
    print("\nFinal Biopics after deletion:")
    for biopic in final_biopics:
        print(biopic)


if __name__ == "__main__":
    main()
