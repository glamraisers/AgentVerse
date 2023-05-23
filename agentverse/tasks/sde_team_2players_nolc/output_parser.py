from __future__ import annotations

import re
from typing import Union

from langchain.agents import AgentOutputParser

# from langchain.schema import AgentAction, AgentFinish

from agentverse.parser import OutputParserError, output_parser_registry, OutputParser
from agentverse.llms.base import LLMResult
from agentverse.utils import AgentAction, AgentFinish


@output_parser_registry.register("sde_team_2players_nolc")
class SdeTeamGivenTestsParser(OutputParser):
    def parse(self, agent, env, output: LLMResult) -> Union[AgentAction, AgentFinish]:
        return AgentFinish({"output": output.content}, output.content)
