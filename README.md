# Visualization

## Miscellaneous
- Visualization Lecture
- Prof.: Bernhard Schmitzer
- Uni Göttingen, summer term 2022, April 17, 2023

## Exercises
- get published roughly once a week
- solutions need to be published to Stud.IP in order to pass the course

## Final Project

### Structure
- [slides / finished graphs](./final-project/slides/pdf/ss23_visualization_mlb.pdf)
- [issue board](https://github.com/users/derMacon/projects/4)
- [main python entrypoint](./final-project/src/vis_main.py)
- [test python package](./final-project/test/)
- [dataset location](./final-project/datasets/retrosheets/game-logs_combined/game_logs_data-world.csv)
   - see *general* section for description on how to download the .csv file

### General
- presentation of the results serves as an oral exam
- available graphs at [./final-project/graphs/](./final-project/graphs/)
- regenerate code by running [`python3 ./final-project/src/vis_main.py`](./final-project/src/vis_main.py)
- dataset source [data world](https://data.world/dataquest/mlb-game-logs)
  - user: `spam-sh` (throwaway account)
  - pass: `abc1234abc1234`
- since the dataset is too large for a GitHub project, download it locally to the following directory
  - `./final-project/datasets/retrosheets/game-logs_combined/game_logs_data-world.csv`

### Progress
- for detailed explanation see the github project [board](https://github.com/users/derMacon/projects/4/views/1)
- available graphs at [./final-project/graphs/](./final-project/graphs/)
- *event plot*: more or less meta information about the dataset
   - attendance per year
   - data per year
   - games per year per team
- *team plot*: more plots
   - home and visiting scores over time
   - winning stats for teams


