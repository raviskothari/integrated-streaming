from typing import Union, Dict

from aws_cdk import (
    core,
    aws_lambda as _lambda
)
from aws_cdk.core import Duration


class IntegratedStreamingStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        test_cdk_lambda_env_var = {
            'LOG_LEVEL': 'INFO'
        }

        self.create_lambda(
            lambda_id='TestLambda',
            path_to_code='integrated_streaming/src/handlers/',
            handler_name='main.handler',
            description='Test lambda function and CDK deployment',
            environment=test_cdk_lambda_env_var,
            function_name='TestCDKLambda',
            timeout=30
        )

    def create_lambda(self, lambda_id: str, path_to_code: str, handler_name: str,
                      description: Union[str, None] = None,
                      environment: Union[Dict, None] = None,
                      function_name: Union[str, None] = None,
                      memory_size: Union[float, int, None] = None,
                      timeout: Union[int] = None) -> None:
        _lambda.Function(
            scope=self,
            id=lambda_id,
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset(path_to_code),
            handler=handler_name,
            description=description,
            environment=environment,
            function_name=function_name,
            memory_size=memory_size,
            timeout=Duration.seconds(timeout)
        )
