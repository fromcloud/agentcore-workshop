from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import calculator
import boto3
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()

# AWS 리전에 따라 Nova Pro 모델 ID 설정
NOVA_PRO_MODEL_ID = "us.amazon.nova-pro-v1:0"
region = boto3.session.Session().region_name
if region.startswith("eu"):
    NOVA_PRO_MODEL_ID = "eu.amazon.nova-pro-v1:0"
elif region.startswith("ap"):
    NOVA_PRO_MODEL_ID = "apac.amazon.nova-pro-v1:0"

@tool
def weather(city: str) -> str:
    """도시의 날씨 정보를 가져옵니다
    Args:
        city: 도시 또는 위치 이름
    """
    return f"{city}의 날씨: 맑음, 35°C"


# 포괄적인 Strands Agent 생성 및 테스트
agent = Agent(
    model=BedrockModel(model_id=NOVA_PRO_MODEL_ID),
    system_prompt = """당신은 간결한 응답을 제공하는 도움이 되는 어시스턴트입니다.
                    """,
    tools=[weather, calculator],
)

@app.entrypoint
async def strands_agent_bedrock(payload, context):
    """
    페이로드로 에이전트를 호출합니다
    """
    print(f"Payload: {payload}")
    print(f"Context: {context}")
    user_input = payload.get("prompt", "프롬프트를 찾을 수 없습니다")
    response = agent(user_input)
    return response

    # 스트리밍 모드
    """
    stream = agent.stream_async(user_input)
    async for event in stream:
        if "data" in event:
            yield event
    """

if __name__ == "__main__":
    app.run()
