import csv
from datetime import datetime

"""
This function reads the product data from the csv file passed to the function in the filename parameter.
 The dictionary key is contained in the csv data column indicated by the key_column_index parameter, 
 the value of each dictionary item is the list derived from the values in the row of the csv file. 
 Function returns a dictionary of products.
"""
def read_dictionary(filename, key_column_index):
    

        dict_key = {}

        with open(filename, mode="rt") as csv_file:
          file_reader = csv.reader(csv_file)
          next(file_reader)
          
          for row in file_reader:
              key = row[key_column_index]
              dict_key[key] = row
        return dict_key
    
def main():
    try:
        subtotal = 0.0
        total_items = 0

        # Step 1: Read the products dictionary (key = product ID)
        products_dict = read_dictionary("products.csv", 0)

        print("Inkom Emporium")
        print()

        # Step 2: Read and process the customer's order
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip header row

            for row in reader:
                if len(row) == 0:
                    continue  # Skip empty lines

                product_id = row[0]
                quantity = int(row[1])

                # Step 3: Look up product info
                product_info = products_dict[product_id]
                name = product_info[1]
                price = float(product_info[2])

                # Print each ordered item
                print(f"{name}: {quantity} @ {price:.2f}")

                # Accumulate totals
                total_items += quantity
                subtotal += quantity * price

        # After the loop: calculate tax and total
        tax = subtotal * 0.06
        total = subtotal + tax

        # Print summary
        print()
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {tax:.2f}")
        print(f"Total: {total:.2f}")
        print()
        print("Thank you for shopping at the Inkom Emporium.")

        # Current date and time
        current_date = datetime.now()
        print(current_date.strftime("%a %b %d %H:%M:%S %Y"))

    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
    except PermissionError:
        print("Error: permission denied")
    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(f"'{e}'")


# Call main
if __name__ == "__main__":
    main()
          


