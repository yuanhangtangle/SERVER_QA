# SVRobot
> @author: Yuanhang Tang (汤远航)
> 
> @e-mail: yuanhangtangle@gmail.com
> 
> @description: a QA robot that provides convenience for issues related to the servers in NLP group

## Pipeline
```mermaid
graph TD
    kw(scan keywords) --> st(state tracking)
    kw --> ei(extract info)
    ei -->|slot:value| fs

    fs(fill slots) -->|lack info| ask(ask for more info)
    ask --> kw
    st --> fs
    fs -->|enough info| ex(excute command)
    ex -->|sth's wrong| re(report error)
    ex -->|more request| kw
```

## Project Structure
- SVRobot
  - NLU
  - SlotValues: 
    - Server
    - user

## Work Flow
```mermaid
graph TD
    guu(get_user_utterance) --> pp(preprocess)
    pp --> ei(extract_info)
    ei --> ts(track_state)
    ts -->|intent changed| rf(clear slots, refill)
    ts -->|intent unchanged| ta(take_action)
    rf --> ta
    ta -->|is_filled| cmd(run_commands)
    ta -->|not is_filled| guu
    cmd --> guu
```

## Todo
> @datetime: 2021/04/09
- Design a NLU strategy and finish `NLU.py`
- Refine `cvRobot.CVRobot.track_state` to use overlapping information
- Design commands to run in the shell
- Add more template response to make it more diverse