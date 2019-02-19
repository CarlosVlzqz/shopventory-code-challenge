
# Import datetime to get the time
from datetime import datetime

'''
When called you can specify the function's time span but if you don't the default time span is 15 minutes.
Eg.  get_account_ids_to_run (account_ids_list, 2) would refresh every 2 minutes
'''

def get_account_ids_to_run(account_ids_list, minutes = 15):

    # Empty list to store the results
    account_ids_to_return = []
    # Get the top limit of the list
    end = account_ids_list[-1]
    # Get the module of the current minute divided by the minutes parameter
    current_minute = datetime.now().minute % minutes

    # int(len(account_ids_list)/minutes + 1) -> gets the max number of items in the return list
    for i in range(int(len(account_ids_list)/minutes) + 1):
        # increment the current id by the minutes times the index of the return list
        current_id = (account_ids_list[current_minute] + ((minutes) * i))
        # if the current id is not greater than the top limit of the id list then add it to the return list
        if current_id < (end + 1):
            account_ids_to_return.append(current_id)

    return(account_ids_to_return)

# Trial list
id_list = [number for number in range(1000, 1100, 1)]
# Function call
print(get_account_ids_to_run(id_list))