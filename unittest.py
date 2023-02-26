import unittest
import tkinter as tk
from tkinter import messagebox
from unittest.mock import patch


from encryption_app import encrypt, decrypt, main_screen


class TestEncryptionApp(unittest.TestCase):
    
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.text1 = tk.Text(self.root)
        self.code = tk.StringVar()
        self.password = "1234"
        
    def test_encrypt(self):
        self.text1.insert(tk.END, "Hello, World!")
        self.code.set(self.password)
        with patch.object(tk, "Toplevel") as mock_top:
            encrypt()
            mock_top.assert_called_with(self.root)
            mock_top().title.assert_called_with("encryption")
            mock_top().geometry.assert_called_with("400x200")
            mock_top().configure.assert_called_with(bg="#ed3833")
            mock_text = mock_top().text2
            mock_text.insert.assert_called_with(tk.END, "SGVsbG8sIFdvcmxkIQ==\n")
    
    def test_decrypt(self):
        self.text1.insert(tk.END, "SGVsbG8sIFdvcmxkIQ==\n")
        self.code.set(self.password)
        with patch.object(tk, "Toplevel") as mock_top:
            decrypt()
            mock_top.assert_called_with(self.root)
            mock_top().title.assert_called_with("decryption")
            mock_top().geometry.assert_called_with("400x200")
            mock_top().configure.assert_called_with(bg="#00bd56")
            mock_text = mock_top().text2
            mock_text.insert.assert_called_with(tk.END, "Hello, World!")
    
    def test_encrypt_invalid_password(self):
        self.text1.insert(tk.END, "Hello, World!")
        self.code.set("wrong_password")
        with patch.object(messagebox, "showerror") as mock_error:
            encrypt()
            mock_error.assert_called_with("encryption", "Invalid Password")
    
    def test_decrypt_invalid_password(self):
        self.text1.insert(tk.END, "SGVsbG8sIFdvcmxkIQ==\n")
        self.code.set("wrong_password")
        with patch.object(messagebox, "showerror") as mock_error:
            decrypt()
            mock_error.assert_called_with("encryption", "Invalid Password")
    
    def test_encrypt_missing_password(self):
        self.text1.insert(tk.END, "Hello, World!")
        self.code.set("")
        with patch.object(messagebox, "showerror") as mock_error:
            encrypt()
            mock_error.assert_called_with("encryption", "Input Password")
    
    def test_decrypt_missing_password(self):
        self.text1.insert(tk.END, "SGVsbG8sIFdvcmxkIQ==\n")
        self.code.set("")
        with patch.object(messagebox, "showerror") as mock_error:
            decrypt()
            mock_error.assert_called_with("encryption", "Input Password")
    
    def test_main_screen(self):
        with patch.object(tk, "mainloop") as mock_loop:
            main_screen()
            mock_loop.assert_called_once()


if __name__ == "__main__":
    unittest.main()
