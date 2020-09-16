data = [('The Phantom Menace', 'Episode I'), ('Attack of the Clones', 'Episode II'), ('Revenge of the Sith', 'Episode III'), ('A New Hope', 'Episode IV'), ('The Empire Strikes Back', 'Episode V'), ('Return of the Jedi', 'Episode VI'), ('The Force Awakens', 'Episode VII'), ('The Last Jedi', 'Episode VIII'), ('The Rise of Skywalker', 'Episode IX')]
def a23(data):
    d = {}
    for a, b in data:
        d.setdefault(a, []).append(b)
    return b