import unittest
import os
import sqlite3
from mylib.transform_load import load
from mylib.query import (
    create_biopic,
    read_biopics,
    update_biopic,
    delete_biopic,
)


class TestDatabaseOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test database and load sample data."""
        # Create a temporary SQLite database for testing
        cls.db_name = "test_biopics.db"
        cls.file_path = "data/test_biopics.csv"

        # Create a mock file with all 14 columns
        with open(cls.file_path, "w", encoding="utf-8") as f:
            f.write(
                "Title,Site,Country,Year,Budget,Director,Number of Subjects,Subject,"
                "Type of Subject,Race Known,Subject Race,Person of Color,Subject Sex,Lead Actor\n"
            )
            f.write(
                "Test Movie,Test Site,Test Country,2024,100000,Test Director,1,"
                "Test Subject,Test Type,Yes,Test Race,No,Female,Test Actor\n"
            )

        # Load data into the test database
        load(cls.file_path)  # Ensure loading into the test DB
        cls.conn = sqlite3.connect(cls.db_name)
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        """Clean up the test database."""
        cls.conn.close()
        os.remove(cls.db_name)
        os.remove(cls.file_path)

    def test_create_biopic(self):
        """Test creating a new biopic record with all 14 columns."""
        create_biopic(
            self.db_name,
            "Test Title",
            "Test Site",
            "Test Country",
            2023,
            "500000",
            "Test Director",
            2,
            "Test Subject",
            "Test Type",
            "Yes",
            "Test Race",
            "No",
            "Female",
            "Test Actor",
        )
        biopics = read_biopics(self.db_name)  # Pass the db_name
        self.assertIn(
            (
                "Test Title",
                "Test Site",
                "Test Country",
                2023,
                "500000",
                "Test Director",
                2,
                "Test Subject",
                "Test Type",
                "Yes",
                "Test Race",
                "No",
                "Female",
                "Test Actor",
            ),
            biopics,
        )

    def test_read_biopics(self):
        """Test reading biopics."""
        biopics = read_biopics(self.db_name)  # Pass the db_name
        self.assertGreater(len(biopics), 0)  # Ensure there are records

    def test_update_biopic(self):
        """Test updating an existing biopic with all 14 columns."""
        # Create a biopic to update
        create_biopic(
            self.db_name,
            "Old Title",
            "Old Site",
            "Old Country",
            2022,
            "300000",
            "Old Director",
            1,
            "Old Subject",
            "Old Type",
            "Yes",
            "Old Race",
            "No",
            "Male",
            "Old Actor",
        )

        # Update biopic
        update_biopic(
            self.db_name,
            "Old Title",
            "Updated Site",
            "Updated Country",
            2023,
            "600000",
            "Updated Director",
            1,
            "Updated Subject",
            "Updated Type",
            "No",
            "Updated Race",
            "Yes",
            "Female",
            "Updated Actor",
        )

        # Verify the update
        updated_biopic = [b for b in read_biopics(self.db_name) if b[0] == "Old Title"]
        self.assertEqual(updated_biopic[0][1], "Updated Site")
        self.assertEqual(updated_biopic[0][8], "Updated Type")

    def test_delete_biopic(self):
        """Test deleting a biopic."""
        create_biopic(
            self.db_name,
            "Delete Title",
            "Delete Site",
            "Delete Country",
            2023,
            "100000",
            "Delete Director",
            1,
            "Delete Subject",
            "Delete Type",
            "Yes",
            "Delete Race",
            "No",
            "Male",
            "Delete Actor",
        )

        delete_biopic(self.db_name)  # Delete by title

        # Verify the deletion
        biopics_after_delete = [
            b for b in read_biopics(self.db_name) if b[0] == "Delete Title"
        ]
        self.assertEqual(len(biopics_after_delete), 0)  # Ensure it's gone


if __name__ == "__main__":
    unittest.main()
