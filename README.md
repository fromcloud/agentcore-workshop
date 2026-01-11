# Bedrock AgentCore와 Strands Agents SDK 및 Nova Pro 워크샵

이 워크샵은 Amazon Bedrock AgentCore에 대한 실습 경험을 제공하며, 다양한 도구와 런타임 환경을 사용하여 정교한 AI 에이전트를 구축하는 방법을 보여줍니다. 코드 인터프리터, 브라우저 자동화, 보안 자격 증명 관리, 메모리 기능을 통합하고 확장 가능한 에이전트 솔루션을 배포하는 방법을 배우게 됩니다.

## 워크샵 개요

워크샵은 서로 연결된 8개의 점진적 실습으로 구성됩니다:

| 실습       | 제목                                       | 설명                                                                                                                 | 주요 학습 포인트                                                                                                                                                                                                                                         | 디렉토리                                                                                            | 파일                                                                                                                                            |
| --------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **실습 0** | Strands Agents 시작하기         | Strands Agents 프레임워크 소개 및 기본 에이전트 생성                                                           | • Strands Agents 기초 학습<br>• 첫 번째 AI 에이전트 생성<br>• 계산기와 같은 내장 도구 사용<br>• 사용자 정의 도구 개발 및 에이전트와 통합                                                                                        | [00-strands-agents/](./00-strands-agents/)                                                           | [00-strands-agents-getting-started.ipynb](./00-strands-agents/00-strands-agents-getting-started.ipynb)                                          |
| **실습 1** | 코드 인터프리터 통합                | 동적 코드 실행 기능을 위해 Strands Agents를 Bedrock AgentCore Code Interpreter와 통합하는 방법 학습       | • 기본 Code Interpreter 기능 테스트<br>• 네트워크 액세스가 있는 사용자 정의 Code Interpreter 생성<br>• 실행 환경 및 제한 사항 비교<br>• AI 에이전트 내에서 Python 코드 동적 실행                                             | [01-bedrock-agentcore-code-interpreter/](./01-bedrock-agentcore-code-interpreter/)                   | [01-agentcore-code-interpreter.ipynb](./01-bedrock-agentcore-code-interpreter/01-agentcore-code-interpreter.ipynb)                              |
| **실습 2** | 브라우저 자동화                          | 웹 상호작용 및 데이터 추출을 위한 브라우저 자동화 기능 탐색                                             | • Strands Agents와 브라우저 자동화 통합<br>• 프로그래밍 방식으로 웹사이트 탐색<br>• 웹 페이지에서 정보 추출<br>• 일반적인 브라우저 자동화 사용 사례 구현                                                                       | [02-bedrock-agentcore-browser/](./02-bedrock-agentcore-browser/)                                     | [02-agentcore-browser-use.ipynb](./02-bedrock-agentcore-browser/02-agentcore-browser-use.ipynb)                                                 |
| **실습 3** | Exa MCP를 사용한 보안 자격 증명 관리   | Exa 검색을 예시로 사용하여 외부 API 통합을 위한 보안 자격 증명 관리 구현                         | • 자격 증명 관리 과제 이해<br>• Exa API용 API Key Credential Providers 생성<br>• 외부 서비스 자격 증명 안전하게 저장 및 검색<br>• Exa MCP 서버로 보안 자격 증명 액세스 테스트                                     | [03-bedrock-agentcore-identity-apikey/](./03-bedrock-agentcore-identity-apikey/)                     | [03-agentcore-identity-for-exa-mcp.ipynb](./03-bedrock-agentcore-identity-apikey/03-agentcore-identity-for-exa-mcp.ipynb)                       |
| **실습 4** | MCP 서버 배포                       | Bedrock AgentCore Runtime에서 Model Context Protocol (MCP) 서버 배포                                                    | • 웹 검색 기능이 있는 사용자 정의 MCP 서버 생성<br>• Amazon Cognito를 사용한 인바운드 인증 설정<br>• AgentCore Runtime에 MCP 서버 배포<br>• Strands Agents로 배포된 MCP 서버 테스트                                             | [04-bedrock-agentcore-runtime-mcp/](./04-bedrock-agentcore-runtime-mcp/)                             | [04-agentcore-runtime-for-mcp-deploy.ipynb](./04-bedrock-agentcore-runtime-mcp/04-agentcore-runtime-for-mcp-deploy.ipynb)                       |
| **실습 5** | 관찰 가능성을 갖춘 에이전트 런타임 배포 | 포괄적인 관찰 가능성 기능을 갖춘 Bedrock AgentCore Runtime에 내장 및 사용자 정의 도구가 있는 Strands Agents 배포 | • 도구가 있는 Strands Agents를 Bedrock AgentCore Runtime에 배포<br>• IAM 권한으로 `boto3` 사용하여 배포된 에이전트 호출<br>• Bedrock AgentCore Runtime 세션의 특성 이해<br>• GenAI 관찰 가능성 및 추적 가능성 학습 | [05-bedrock-agentcore-runtime-and-observability/](./05-bedrock-agentcore-runtime-and-observability/) | [05-agentcore-runtime-for-strands-deploy.ipynb](./05-bedrock-agentcore-runtime-and-observability/05-agentcore-runtime-for-strands-deploy.ipynb) |
| **실습 6** | 메모리 통합                          | Bedrock AgentCore Memory를 사용하여 Strands Agents와 지속적인 메모리 기능 통합                                 | • AI 에이전트의 메모리 개념 이해<br>• 단기 및 장기 메모리 구현<br>• 대화 연속성을 위한 메모리 지원 에이전트 생성<br>• 세션 간 메모리 검색 테스트                                                         | [06-bedrock-agentcore-memory/](./06-bedrock-agentcore-memory/)                                       | [06-agentcore-memory.ipynb](./06-bedrock-agentcore-memory/06-agentcore-memory.ipynb)                                                            |
| **실습 7** | OpenAPI를 사용한 게이트웨이 통합            | Bedrock AgentCore Gateway를 사용하여 OpenAPI 사양에서 MCP 서버 자동 생성                             | • 게이트웨이 액세스를 위한 Cognito 인바운드 인증 생성<br>• MCP 서버 생성을 위한 OpenAPI 사양 업로드<br>• 아웃바운드 인증을 위한 API 키 자격 증명 공급자 구성<br>• Strands Agents로 생성된 MCP 서버 테스트             | [07-bedrock-agentcore-gateway-openapi/](./07-bedrock-agentcore-gateway-openapi/)                     | [07-agentcore-gateway-for-exa-openapi.ipynb](./07-bedrock-agentcore-gateway-openapi/07-agentcore-gateway-for-exa-openapi.ipynb)                 |

## 사전 요구사항

워크샵을 시작하기 전에 다음이 준비되어 있는지 확인하세요:

- **AWS 계정** - Bedrock AgentCore 및 관련 서비스에 대한 적절한 권한 포함
  - `BedrockAgentCoreFullAccess` 관리형 정책
  - `AmazonBedrockFullAccess` 관리형 정책
  - `CloudWatchFullAccess` 관리형 정책 
  - `호출자 권한`: 자세한 정책은 [여기](https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/user-guide/runtime/permissions.md#developercaller-permissions)를 참조하세요
- Bedrock에서 [Amazon Nova Pro 모델 액세스](https://docs.aws.amazon.com/nova/latest/userguide/getting-started-console.html) 요청
- AgentCore 관찰 가능성을 위한 [CloudWatch Transaction Search 활성화](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html#observability-configure-builtin)
- **AWS 자격 증명** 구성 (IAM 역할 또는 환경 변수) 
- **Python 환경** - 필요한 패키지 포함 (`pyproject.toml`에 나열되고 각 노트북에 지침 포함)
- **Exa API 키** (실습 3 및 7에 필요) - [Exa 대시보드](https://dashboard.exa.ai/api-keys)에서 획득

### AWS 리전

이 워크샵에는 `us-east-1` 사용을 권장합니다. Bedrock AgentCore는 특정 AWS 리전에서 사용할 수 있습니다. 지원되는 리전에서 작업하고 있는지 확인하세요.

### 환경 설정

IAM 역할을 사용하지 않는 경우 AWS 자격 증명을 구성하세요:

```python
import os

os.environ["AWS_ACCESS_KEY_ID"] = "<YOUR_ACCESS_KEY>"
os.environ["AWS_SECRET_ACCESS_KEY"] = "<YOUR_SECRET_KEY>"
os.environ["AWS_SESSION_TOKEN"] = "<OPTIONAL_SESSION_TOKEN>"
os.environ["AWS_REGION"] = "<AWS_REGION>"
```

## 워크샵 구조

```
sample-bedrock-agentcore-with-strands-and-nova/
├── 00-strands-agents/
│   └── 00-strands-agents-getting-started.ipynb
├── 01-bedrock-agentcore-code-interpreter/
│   └── 01-agentcore-code-interpreter.ipynb
├── 02-bedrock-agentcore-browser/
│   └── 02-agentcore-browser-use.ipynb
├── 03-bedrock-agentcore-identity-apikey/
│   └── 03-agentcore-identity-for-exa-mcp.ipynb
├── 04-bedrock-agentcore-runtime-mcp/
│   ├── 04-agentcore-runtime-for-mcp-deploy.ipynb
├── 05-bedrock-agentcore-runtime-and-observability/
│   ├── 05-agentcore-runtime-for-strands-deploy.ipynb
├── 06-bedrock-agentcore-memory/
│   ├── 06-agentcore-memory.ipynb
├── 07-bedrock-agentcore-gateway-openapi/
│   ├── 07-agentcore-gateway-for-exa-openapi.ipynb
│   └── exa-openapi-spec.yaml
├── pyproject.toml
├── uv.lock
└── README.md
```

## 시작하기

1. **AWS 자격 증명을 설정**하고 지원되는 리전에 있는지 확인하세요
2. **uv**로 워크샵 환경 설정 - [uv 설치](https://docs.astral.sh/uv/getting-started/installation/)
   ```bash
   uv sync
   ```
3. **실습 0부터 시작**하여 실습을 순차적으로 진행하세요
4. **각 실습을 완료**하여 AWS 리소스를 정리하세요

> **참고:** 불필요한 요금을 피하기 위해 워크샵 중에 생성된 AWS 리소스를 정리해야 합니다. 각 실습에는 해당하는 경우 정리 지침이 포함되어 있습니다.

## 주요 학습 성과

이 워크샵을 완료하면 다음을 할 수 있습니다:

- Strands Agents 기초 및 프레임워크 이해
- 코드 실행 기능이 있는 AI 에이전트 구축
- 웹 상호작용을 위한 브라우저 자동화 구현
- 외부 서비스 통합을 위한 자격 증명 안전하게 관리
- 프로덕션 환경에서 MCP 서버 배포 및 확장
- 관찰 가능성을 갖춘 포괄적인 에이전트 솔루션 생성
- 대화 연속성을 위한 지속적인 메모리 기능 통합
- Gateway를 사용하여 OpenAPI 사양에서 MCP 서버 생성
- 에이전트 개발 및 배포를 위한 모범 사례 적용

## 지원 및 리소스

- [Amazon Bedrock AgentCore 개발자 가이드](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/)
- [Amazon Bedrock AgentCore 샘플](https://github.com/awslabs/amazon-bedrock-agentcore-samples)
- [Strands Agents SDK](https://strandsagents.com/latest/)
- [Strands Agents 샘플](https://github.com/strands-agents/samples)
- [Amazon Bedrock 사용자 가이드](https://docs.aws.amazon.com/bedrock/latest/userguide/)
- [Amazon Nova 사용자 가이드](https://docs.aws.amazon.com/nova/latest/userguide/)

---

## 기여

커뮤니티 기여를 환영합니다! 가이드라인은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참조하세요.

## 보안

자세한 정보는 [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications)을 참조하세요.

## 라이선스

이 라이브러리는 MIT-0 라이선스에 따라 라이선스가 부여됩니다. [LICENSE](LICENSE) 파일을 참조하세요.