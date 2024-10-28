calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(name):
    global calls
    calls += 1
    p = len(name), name.upper(), name.lower()
    print(p)
def is_contains(string, list_to_search):
    global calls
    calls += 1
    a = False
    for i in list_to_search:
        if i.upper() == string.upper():
            a = True
    print(a)
string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic']) # No matches
print(calls)