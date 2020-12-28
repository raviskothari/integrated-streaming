#!/usr/bin/env python3

from aws_cdk import core

from integrated_streaming.integrated_streaming_stack import IntegratedStreamingStack


app = core.App()
IntegratedStreamingStack(app, "integrated-streaming")

app.synth()
