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
    - one intent for several actions: to mount several disks for different servers, to add several users
    - several intents: to mount a disk and also add a user
    - combination of the above

## Todo
- Finish `NLU.py`
- Refine `cvRobot.CVRobot.track_state` to use overlapping information
- Design commands to run in the shell
- Add a server profile and modify extracter
------------------------

> @datetime: 2021/04/12
## Todo
- Finish `NLU.extract_user_info`
- `svRobot.state` and `svRobot.slots.intent`
- Refine `cvRobot.CVRobot.track_state` to use overlapping information
- Design commands to run in the shell
-----------------------

> @datetime: 2021/04/15

## Project Structure
- __test__.json
- SVRobot
- NLU
  - profiles/intents.josn
  - profiles/disks.json
  - profiles/servers.json
- SlotValues
  - Server
  - User
  - Disk

- utils

## More Ideas
- Summarize key match methods (done)
- Record user dialogues history
- A better implementation for state tracking
- A better strategy for information update
- May compute confidence or set confidence level when it is not easy to design priority-based match methods.
- What if a single utterance contains more than one intent?
- DAG may be introduced to modeled step-by-step strategy

## Key Match Strategy:
- server: key word matching + regular expression matching 
- disk: key word matching + auxiliary word match
- intent: key word matching
  
```mermaid
graph LR
    ms(matching strategy) --> mss(multi-step strategy)
    sss(single-step strategy) --> intent
    ms --> sss
    mss --> server
    server --> skw(key word matching)
    skw --> rg(regular expression matching)
    mss --> disk
    disk --> dkw(key word matching)
    dkw --> aw(auxiliary word matching)
```

**Multi-step matching strategy** can be viewed as breaking down a pattern into low-level patterns and match those low-level patterns step-by-step. The confidence on a pattern is increased if some of the low-level patterns are matched, and what patterns will be used depends on the previous matching results. Possible patterns are decreased during this process. This process can be naturally modeled by a DAG. 

Advantages:

- Underlying priority
- Reduce redundant matching
- Define confidence level naturally

Disadvantages:

- Human efforts
- May meet unseen patterns
- Only effective for simple scenes