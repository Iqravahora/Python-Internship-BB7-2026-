admin = {"read", "write", "delete"}
editor = {"read", "write"}

can_delete = "delete" in editor
print("can editor delete:", can_delete)

print("has all admin permission?", admin.issubset(editor))

