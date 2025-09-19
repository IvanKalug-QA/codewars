# Description:
# Oh no! The celestial bodies orbiting the sun are all jumbled up!
#
# TASK
# Given the entire Solar System in the form of a list. Return a new list which has either '<', '>' or '=' depending on whether the planet is smaller than the planet on its left or not. You have to start comparing from the second item, because the first has nothing on its left.
# However, there are also asteroids in the Solar System. All asteroids are smaller than all the planets. If two asteroids are found beside each other, the leftmost one will depend on the celestial being on the left of it. The one on the right will have '='.
#
# The Solar System might be empty.
#
# The celestial bodies stand in the order (size ascending):
#
# Asteroid < Pluto < Mercury < Mars < Venus < Earth < Neptune < Uranus < Saturn < Jupiter
#
# Important: the dwarf planet Pluto is also included in the Solar System
#
# EXAMPLES
# ["Mars", "Asteroid", "Venus", "Jupiter", "Asteroid", "Earth", "Pluto"] -> ['<', '>', '>', '<', '>', '<']
# # Asteriod is '<' Mars
# # Venus is '>' any Asteroid
# # Jupiter is '>' Venus
# # Any Asteroid is '<' Jupiter
# # Earth is '>' the Asteroid
# # Finally, Pluto, being a dwarf planet, is '<' Earth
#
# ["Asteroid", "Asteroid", "Asteroid", "Earth", "Jupiter"] -> ['=', '=', '>', '>']
# # Here, the Asteroid is '=' to the Asteroid on its left
# # Again, it is '=' because there is another Asteroid on its left
# # Earth is '>' than the Asteroid
# # Finally, Jupiter, being the king of the planets, is '>' than Earth
#
# ["Mercury", "Venus", "Earth", "Mars", "Asteroid", "Jupiter", "Saturn", "Uranus", "Neptune", "Asteroid", "Pluto"] -> ['>', '>', '<', '<', '>', '<', '<', '<', '<', '>']
# # Atleast here the Solar System is how it's supposed to be!
# NOTES
# There will never be more than one of anything except asteroids
#
# The Solar System will never contain anything outside:
#
# ["Asteroid", "Pluto", "Mercury", "Mars", "Venus", "Earth", "Neptune", "Uranus", "Saturn", "Jupiter"]

def jumbled_solar_system(solar_system):
    d = {
        'Asteroid': 0, 'Pluto':1,
        'Mercury': 2, 'Mars': 3,
        'Venus': 4, 'Earth': 5,
        'Neptune': 6, 'Uranus': 7,
        'Saturn': 8, 'Jupiter': 9,
    }
    result = []
    if not solar_system or len(solar_system) == 1:
        return []
    for i in range(1, len(solar_system)):
        if d[solar_system[i]] > d[solar_system[i-1]]:
            result.append('>')
        elif d[solar_system[i]] < d[solar_system[i-1]]:
            result.append('<')
        else:
            result.append('=')
    return result
