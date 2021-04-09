# Paper Notes

> @author:  汤远航 (Yuanhang Tang)
>
> @e-mail: yuanhangtangle@gmail.com

## A Survey on Dialogue Systems:Recent Advances and New Frontiers

> @datetime: 2021/04/03
>
> @link: https://arxiv.org/abs/1711.01731

This paper gives an overview to dialogue systems. More specifically, this paper categorizes DS into two main kinds: task-oriented system and non-task-oriented system. See the graph below for more details:

```mermaid
graph LR
	ds(Dialogue System) --> to(task-oriented)
	to --> pm(pipeline method)
	pm --> nlu(natural Language understanding)
	pm --> dst(dialogue state tracker)
	pm --> dpl(dialogue policy learning)
	pm --> nlg(natural language generation)
	to --> to_eem(end-to-end method)
	to_eem --> eem_des(single module mapping input<br> history to system output)
	ds --> nto(none-task-oriented)
```

### Task-Oriented System

Assist the user to complete some task

- **NLU** (**Natural language understanding**): 
	extract information from  user utterance.
  - Maps the user utterance into **predefined slots**. A slot is a concept ID, e.g. location, date time, etc. **Slot filling** assigns each input word with a predefined semantic label. It takes a sentence as input and output a sequence of slots. one for each word in the input sentence. This can be modeled as a **sequence labeling problem** similar to the POS tagging problem.
  - Classifies the user intent into **predefined intent** or detect dialogue **domain**. This is simply a classification problem. Statistical method or deep learning method can be applied to address this issue.
  - The semantic representation generated in this step is passed to the next step.

- **Dialogue state tracking**: 
	The user's goal may change during the conversation, and this can be modeled as a **state struture** similar to the one adopted in NAOGOLF. According to semantic representation generated in the last step, a state management system (**rule-based system**, **statistic dialog system** or **deep learning based dialog model**) mantains a state struture and categorizes the current situation into one of the predefined states (commonly called **semantic frame** or **slot**) by combining the previous system acts, dialogue history and previous dialogue states. This is the core component to ensure a robust manner.
	- **rule-based system**: Like what we do in NAOGOLF;
	- **statistical method**: Mantains a distribution over predefined slots, and output the most likely one;
	- **deep learning based methodd**: Just train it;

- **Policy learning**:
	Conidtioned on the state representation, policy learning component generates the next system action. **Rule-based method**, **supervised learning method** or **reinforcement learning method** can be adopted to choose one of **predefined action** based on current state. This module may interates with a external database to generate meaningful action.

- **NLG** (**natural language generation**):
	Conditioned on the chosen action, state and other representation from the upstream modules, NLG module converts this semantic symbols into natura language and present the result to the user. 
	- Conventional method typically adopt a **sentence planning system** which first convert the semantic symbols to intermediary form such as template or tree-like structures and then convert them into final response.
	- Deep learning based model: Just train it.

- **End-to-End Method**:
	End-to-end model uses a single module to map the dialogue history to the final response.

- **Shortcomings**:
	A task-oriented dialogue system aims at asssiting the use to complete some task, thus it is usually related to some certain domain, e.g. shopping, custom service, etc. A conventional rule-based dialogue system is usually specialized with **interdependent components**, and **does not promise portability**. **Significant human effort**, including **data collection**, labeling, rule design, template design and so on, must be devoted to create such a system. Moreover, it is **hard to design update method** for such systems since operations like **querying external database** are **non-differentiable**, and the user's feedback is hard to be **propagated to upstream modules**.

- **Techniques**: 
	- **rule design**: 
		- Like what we do in NAOGOLF
	- **statistical methods**:
		- Output the probability of each slot for each input word
		- Output the probability for each predefined intent or domain
	- **supervised learning methods**:
		- End-to-End model: replace non-differentiable operations with differentiable layers
		- Classification model
	- **reinforcement learning methods**:
		- Model the dialogue system as an intelligent agent interacting with the user
	- **Generalization and Specialization**:
		- Generalization for portability, specialization for good performance
		- *Pre-train and fine-tune*

### Non-Task-Oriented System
Take with the user on open domains; Chatting robot such as Xiaoai, Siri, etc

- **Neural Generative Models**: sequence-to-sequence models
	- capture dialogue context
	- increase response diversity, reduce meaningless responses:
		- modify decoder
		- design better objective function
		- introduce **latent variables** to mantain a distribution
		- model dialogue topic and the user's personality
		- query knowledge database
	- learning throught interaction

- **Retrival-based Methods**:
	- choose a response from predefined responses
	- a repsonse match problem: single turn or multi-turn

- **evaluation**: hard to automatically evaluate; some criteria
	- forward-looking
	- informative
	- coherent
	- interactint