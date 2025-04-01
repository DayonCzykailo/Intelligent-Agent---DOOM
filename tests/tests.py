import os, vizdoom as vd
from time import sleep
from random import choice

actions = [[True, False, False], [False, True, False], [False, False, True]]
sleep_time = 1.0 / vd.DEFAULT_TICRATE 

# plan



if __name__ == "__main__":
    game = vd.DoomGame()
    game.set_doom_scenario_path(os.path.join(vd.scenarios_path, "basic.wad"))
    game.set_doom_map("map01")
    game.set_screen_resolution(vd.ScreenResolution.RES_640X480)
    game.set_available_buttons([vd.Button.MOVE_LEFT, vd.Button.MOVE_RIGHT, vd.Button.ATTACK])
    game.set_episode_timeout(200)
    game.set_episode_start_time(10)
    game.set_living_reward(-1)


    print("Available buttons:", [b.name for b in game.get_available_buttons()])

    game.init()


    episodes = 10

    for i in range(episodes):
        print(f"Episode {i + 1}/{episodes}")

        game.new_episode()

        while not game.is_episode_finished():

            state = game.get_state()

            print(f"State #{state.number}")
            print(f"Game variables: {state.game_variables}")
            print(f"Labels: {state.labels}")
            print(f"Depth buffer: {state.depth_buffer}")
            print(f"Automap buffer: {state.automap_buffer}\n")

            number = state.number
            vars = state.game_variables

            screen_buf = state.screen_buffer
            depth_buf = state.depth_buffer
            labels_buf = state.labels_buffer
            automap_buf = state.automap_buffer
            audio_buf = state.audio_buffer

            labels = state.labels
            objects = state.objects
            sectors = state.sectors

            r = game.make_action(choice(actions))

            print("Game variables:", vars)
            print("Reward:", r)

            if sleep_time > 0:
                sleep(sleep_time)

        game.close()
    
    print("Game closed.")