# SVRobot
> @author: Yuanhang Tang (汤远航)
> 
> @e-mail: yuanhangtangle@gmail.com
> 
> @description: a QA robot that provides convenience for issues related to the servers in NLP group
--------------------------

> @datetime: 2021/04/09
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
- Design a NLU strategy and finish `NLU.py`
- Refine `cvRobot.CVRobot.track_state` to use overlapping information
- Design commands to run in the shell
- Add more template response to make it more diverse
-------------------------------

> @datetime: 2021/04/11

```mermaid
graph LR 
    subgraph Server_List
        sv(server) --> 1080ti
        sv --> 2080ti
        sv --> titan
        1080ti --> 1-6
        2080ti --> 1-2
        titan --> 1,3,rtx

        disk --> data_ti* 
        data_ti* --> 4c,4d
        data_ti* --> 5c,5d
        disk --> user_data_182*
        user_data_182* --> a,b
        disk --> *_data
        *_data --> nlper,public,user
    end

```

```mermaid
graph LR 
    subgraph disks
        182 -->|Y|ab[182a,182b]
        182 -->|N|npu[nlper,public,user]
        npu -->|N|cd[4c,4d,5c,5d]
        cd -->|Y|data_ti
        cd -->|N|adn[ask_disk_info]
        data_ti -->|N| cdd(confirm_disk_data)
        npu -->|Y|done
        data_ti -->|Y|done((done))
        ab -->|Y|done
        ab -->|N|cdd
    end
```

```mermaid
graph LR
    subgraph Intent
        diao[掉,挂] --> md[mount_disk]
        user[账号,用户,注册] --> adduser
    end
```

## Possible Requests
  - one request for a single utterance: to mount exactly one disk, to add exactly one user
  - several requests for a single utterance: 
    - one intent for sreveral actions: to mount several disks for different servers, to add several users
    - several intents: to mount a disk and also add a user
    - combination of the above

## Todo
- Finish `NLU.py`
- Refine `cvRobot.CVRobot.track_state` to use overlapping information
- Design commands to run in the shell
- Add more template response to make it more diverse
- Replace priority of each intents with probability
- Add a server profile and modify extracter