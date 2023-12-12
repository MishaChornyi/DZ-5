import colorama

print("Атрибути:")
for colo in dir(colorama):
    print(f"- {colo}")
print("\nМетоди:")
for colo in dir(colorama.Fore):
    print(f"- {colo}")