from aws_cdk import (
    Stage,
    )
import aws_cdk as cdk
from constructs import Construct
from sprint3.sprint3_stack import Sprint3Stack

class MyStage(Stage):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # These stages will point towards my application stack whic is our sprint3 stack
        self.stage = Sprint3Stack(self, "MureedAppStack")