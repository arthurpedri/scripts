def reverse_quotes(quotes):
    # Reverse the list of quotes
    reversed_quotes = quotes[::-1]
    return reversed_quotes

def read_quotes_from_file(file_name):
    with open(file_name, 'r') as file:
        quotes = file.read().split('\n\n')  # Split quotes by two line breaks
        quotes = [quote.strip() for quote in quotes]  # Remove leading/trailing whitespace
    return quotes

# Input file containing quotes separated by two line breaks
file_name = 'input_quotes.txt'

# Read quotes from the input file
quotes = read_quotes_from_file(file_name)
print(len(quotes))
# Reverse the order of quotes
reversed_quotes = reverse_quotes(quotes)

# Print the reversed quotes
for quote in reversed_quotes:
    print(quote)
    print()
