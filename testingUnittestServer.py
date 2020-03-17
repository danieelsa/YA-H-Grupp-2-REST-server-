import unittest
import server

class TestServerMethods(unittest.TestCase):

    def test_add_file1(self):
        file_name = "file_on_server.txt"
        output =  server.add_file(file_name)

        self.assertEqual(output, ("", 201))

    def test_add_file2(self):
        file_name = "file/document/not_a_file_on_server.txt"
        output =  server.add_file(file_name)

        self.assertEqual(output, 400)
    
    def test_delete_file1(self):
        # get name of an excicting file on server.   
        output = server.delete_file("file_on_server.txt")
        
        self.assertEqual(output, ('', 200))
        
    def test_delete_file2(self):
        # get name of non-excicting file on server.
        output = server.delete_file("file/document/not_a_file_on_server.txt")
        
        self.assertEqual(output, ('', 404))


if __name__ == '__main__':
    unittest.main()
