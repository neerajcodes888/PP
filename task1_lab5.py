def list_to_dict(lst):
  if not lst:
    return {}
  if len(lst) == 1:
    return lst[0]
  return {lst[0]: list_to_dict(lst[1:])}


my_list = ['a', 'b', 'c', 'd']
my_dict = list_to_dict(my_list)
print(my_dict)
