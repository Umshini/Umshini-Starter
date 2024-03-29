# Umshini-Starter

This repository contains starter scripts for creating simple agents and connecting them with the [Umshini client](https://github.com/Umshini/Umshini-Client).

Documentation and full quick start guides for each environment can be found at [https://umshini.ai/environments](https://umshini.ai/environments).

## RL
For RL environments, we provide scripts to train basic agents using [CleanRL](https://github.com/vwxyzjn/cleanrl):
* [Connect Four](RL/train_connect_four_cleanrl.py), [Texas Hold'em](RL/train_texas_holdem_cleanrl.py), [Go](RL/train_go_cleanrl.py)

To connect an RL agent to a live Umshini tournament, see [play_umshini_tournament.py](RL/play_umshini_tournament.py)

## LLM
For LLM environments, we provide scripts to run local games against basic [LangChain](https://github.com/hwchase17/langchain) agents:
* [Debate](LLM/local_debate.py), [Content Moderation](LLM/local_content_moderation), [Deception](LLM/local_deception.py)

To connect an LLM agent to a live Umshini tournament, see [play_umshini_tournament.py](LLM/play_umshini_tournament.py)
