lista = ['Coco', 'Princess', 'Samantha', 'Sheba', 'Abby', 'Gizmo', 'Lilly', 'Sammy', 'Pumpkin', 'Cali', 'Rascal', 'Toby', 'Luna', 'Boo', 'Mittens', 'Buddy', 'Pepper', 'Maggie', 'Daisy', 'Spooky', 'Samantha', 'Boo', 'Kiki', 'Mia', 'Boo', 'Dusty', 'Boo', 'Buster', 'Luna', 'Buster', 'Sheba', 'Angel', 'Pumpkin', 'Baby', 'Garfield', 'Maggie', 'Annie', 'Tinkerbell', 'Missy', 'Scooter', 'Buster', 'Toby', 'Muffin', 'Bailey', 'Tigger', 'Oscar', 'Lucy', 'Shadow', 'Chloe', 'Lilly', 'Chester', 'Midnight', 'Max', 'Trouble', 'Whiskers', 'Jasper', 'Mimi', 'Charlie', 'Precious', 'Bandit', 'Boots', 'Dusty', 'Snuggles', 'Zoe', 'Scooter', 'Mimi', 'Peanut', 'Mimi', 'Jasper', 'Felix', 'Oreo', 'Cuddles', 'Kitty', 'Tigger', 'Oscar', 'Sadie', 'Bubba', 'Smokey', 'Cookie', 'Snuggles', 'Whiskers', 'Misty', 'Sheba', 'Missy', 'Bear', 'Coco', 'Max', 'Cuddles', 'Loki', 'Baby', 'Toby', 'Casper', 'Oliver', 'Sugar', 'Pepper', 'Chloe', 'Buster', 'Milo', 'Kiki', 'Mia']
dicionario = {}

for i in lista:
    if i not in dicionario:
        dicionario[i] = 1
    else:
        dicionario[i] += 1

for k, v in dicionario.items():
    if v > 1:
        print(f'A palavra {k} repete {v} vezes.')