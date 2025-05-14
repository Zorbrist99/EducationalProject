# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

a= [1, 2, 3, 4, 5]
print(a)
print(len(a))
print(a[1])
print("-----------")

a.append(1)
print(a)
print("-----------")
a.insert(1, 10)
print(a)
print("-----------")
a.pop(2)
print(a)
print("-----------")
words = ["python", "java", "c++", "go", "kotlin", "rust"]
print(words[0:3])
print("-----------")
print(words[::-1])
print("-----------")
print(words[:3])