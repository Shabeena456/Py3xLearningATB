def allowed_to_attend_class(name, password):

    if name == "shabeena" :
        if password == "yes":
           print("allowed")
        else:
           print("mot allowed")

allowed_to_attend_class("shabeena","yes")



# def allowed_to_attend_python_class(name):
#
#
#  match name:
#
#     case "DELL":
#
#      print("Dell is allowed")
#
#     case "Shubham":
#
#      print("Shubham is allowed")
#
#     case "Pallavi":
#
#      print("Pallavi is allowed")
#
#     case _:
#
#      print("Not Allowed")
#
# allowed_to_attend_python_class("DELL")
