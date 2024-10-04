import unittest
import os
import sqlite3
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


class TestDatabaseOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test database and load sample data."""
        # Create a temporary SQLite database for testing
        cls.db_name = "test_biopics.db"
        cls.file_path = "data/test_biopics.csv"

        # Extract sample data (can create a mock file for testing)
        extract(
            url="https://github.com/fivethirtyeight/data/raw/refs/heads/master/biopics/biopics.csv",
            file_path=cls.file_path,
        )
        load(cls.file_path)  # Load data into the actual test database
        cls.conn = sqlite3.connect(cls.db_name)
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        """Clean up the test database."""
        cls.conn.close()
        os.remove(cls.db_name)

    def test_create_biopic(self):
        """Test creating a new biopic record."""
        query.create_biopic(
            "Test Title", "Test Site", "Test Country", 2023, "500000", "Test Director"
        )
        biopics = query.read_biops()
        self.assertIn(
            (
                "Test Title",
                "Test Site",
                "Test Country",
                2023,
                "500000",
                "Test Director",
            ),
            biopics,
        )

    def test_read_biopics(self):
        """Test reading biopics."""
        biopics = query.read_biopics()
        self.assertGreater(len(biopics), 0)  # Ensure there are records

    def test_update_biopic(self):
        """Test updating an existing biopic."""
        # Create a biopic to update
        query.create_biopic(
            "Old Title", "Old Site", "Old Country", 2022, "300000", "Old Director"
        )
        # Read and get the ID of the new biopic
        biopics = query.read_biopics()
        biopic_id = biopics[-1][0]  # Get the ID of the last biopic
        query.update_biopic(
            biopic_id,
            "Updated Title",
            "Updated Site",
            "Updated Country",
            2023,
            "600000",
            "Updated Director",
        )

        # Verify the update
        updated_biopic = query.read_biopics()[-1]  # Get the last biopic
        self.assertEqual(updated_biopic[1], "Updated Title")

    def test_delete_biopic(self):
        """Test deleting a biopic."""
        query.create_biopic(
            "Delete Title",
            "Delete Site",
            "Delete Country",
            2023,
            "100000",
            "Delete Director",
        )
        biopics = query.read_biopics()
        biopic_id = biopics[-1][0]  # Get the ID of the last biopic
        query.delete_biopic(biopic_id)

        # Verify the deletion
        biopics_after_delete = query.read_biopics()
        self.assertNotIn(
            biopic_id, [b[0] for b in biopics_after_delete]
        )  # Check ID is not present


if __name__ == "__main__":
    unittest.main()
