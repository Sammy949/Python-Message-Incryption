from tkinter import Tk, messagebox, simpledialog
import pyperclip

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + '#'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)

    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

def remove_extra_character(message):
    # Remove the '#' if it exists at the end of the message
    if message.endswith('#'):
        message = message[:-1]
    return message

def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt')
    return task

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

root = Tk()
root.withdraw()  # Hide the root window

while True:
    task = get_task()

    if task in ('encrypt', 'Encrypt'):
        message = get_message()
        encrypted = swap_letters(message)
        pyperclip.copy(encrypted)  # Copy to clipboard
        messagebox.showinfo('Encrypted Message', f'Message in encrypted version is: {encrypted}\n\nThe message has been copied to the clipboard!')

    elif task in ('decrypt', 'Decrypt'):
        message = get_message()
        decrypted = swap_letters(message)
        decrypted = remove_extra_character(decrypted)  # Remove the extra character if present
        messagebox.showinfo('Decrypted Message', f'Message in decrypted version: {decrypted}')

    else:
        break

root.mainloop()
