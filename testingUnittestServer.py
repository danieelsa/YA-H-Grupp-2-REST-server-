import unittest
import server

class TestServerMethods(unittest.TestCase):

    # This test should work, because the "PUT"-command replace the old file with this file,
    # even if the files have the same name.
    def test_add_file1(self):
        file_name = "file_on_server.txt"
        output =  server.add_file(file_name)

        self.assertEqual(output, ("", 201))

        
    def test_add_file2(self):
        file_name = "not_a_file_on_server.txt"
        output =  server.add_file(file_name)

        self.assertEqual(output, ("", 201))

        
    def test_add_file3(self):
        file_name = "file/document/not_a_file_on_server.txt"
        output =  server.add_file(file_name)

        self.assertEqual(output, 400)
    
    
    def test_delete_file1(self):
        # delete an existing file on server.   
        output = server.delete_file("file_on_server.txt")
        
        self.assertEqual(output, ('', 200))
       
    
    def test_delete_file2(self):
        # delete an non-existing file on server.
        output = server.delete_file("file/document/not_a_file_on_server.txt")
        
        self.assertEqual(output, ('', 404))


    def test_get_file1(self):
        # get an existing file on server
        output = server.get_file("file_on_server.txt")
        
        # VAD SKA DET STÅ HÄR???
        
        
if __name__ == '__main__':
    unittest.main()
