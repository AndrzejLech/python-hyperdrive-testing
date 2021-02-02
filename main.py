from src.galaxyAtlasBuilder import GalaxyAtlasBuilder
from src.hyperdriveNavigator import HyperdriveNavigator

if __name__ == '__main__':
    atlas = GalaxyAtlasBuilder().build_from_yml('resources/routes.yml')
    hyperdrive = HyperdriveNavigator(atlas)

    target = hyperdrive.get_random_planet()

    print('Your target is the ' + target.name)

    planet = hyperdrive.get_random_planet()

    while True:
        planet = hyperdrive.get_current_planet()

        if planet == target:
            print('You\'ve reached your target!')
            break

        print('Your on the ' + planet.name + '. You can jump to:')
        for index, neighbour in enumerate(planet.neighbours):
            print(str(index) + '.', neighbour.name)
        answer = input()
        if int(answer) < len(planet.neighbours):
            hyperdrive.jump_to(planet.neighbours[int(answer)])
        if answer == 'quit':
            break
