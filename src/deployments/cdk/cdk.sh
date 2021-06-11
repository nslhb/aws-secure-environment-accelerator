#!/bin/sh

export CONFIG_MODE="development"
export CDK_PLUGIN_ASSUME_ROLE_NAME="nsl-PipelineRole"
export AWS_PROFILE=roota
export BOOTSTRAP_STACK_NAME=nsl-CDKToolkit
pnpx ts-node --transpile-only cdk.ts $@