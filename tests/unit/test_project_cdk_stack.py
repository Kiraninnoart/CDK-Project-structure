import aws_cdk as core
import aws_cdk.assertions as assertions

from project_cdk.project_cdk_stack import ProjectCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in project_cdk/project_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ProjectCdkStack(app, "project-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
