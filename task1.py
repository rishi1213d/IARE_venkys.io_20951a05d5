import threading

def reverse_substring(s):
    if len(s) <= 1:
        return s
    else:
        mid = len(s) // 2
        left = s[:mid]
        right = s[mid:]
      
        left_thread = threading.Thread(target=reverse_substring, args=(left,))
        right_thread = threading.Thread(target=reverse_substring, args=(right,))
        left_thread.start()
        right_thread.start()
      
        left_thread.join()
        right_thread.join()
        
        return right[::-1] + left[::-1]


paragraph = input("Enter a paragraph: ")


reversed_paragraph = reverse_substring(paragraph)

print(reversed_paragraph)
