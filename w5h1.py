import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# API-KEY 입력 받기
api_key = st.text_input("API-KEY를 입력하세요.")

# 육하원칙 입력 칸 개발
st.title("육하원칙 작문기")
st.write("육하원칙에 해당하는 내용을 입력하세요.")
who = st.text_input("누가?")
what = st.text_input("무엇을?")
when = st.text_input("언제?")
where = st.text_input("어디서?")
why = st.text_input("왜?")
how = st.text_input("어떻게?")

# 생성 버튼 개발
if st.button("생성"):

    # Gemini Pro 모델 초기화
    llm = ChatGoogleGenerativeAI(
        google_api_key=api_key,
        model="gemini-pro",
        temperature=0.7
    )

    # 프롬프트 템플릿 생성
    template = "{who}가 {what}을 {when}에 {where}에서 {why}로 {how}로 합니다."
    prompt = PromptTemplate(
        input_variables=["who", "what", "when", "where", "why", "how"],
        template=template
    )

    # LLMChain 대신 직접 llm.predict 사용
    final_prompt = prompt.format(
        who=who, what=what, when=when, 
        where=where, why=why, how=how
    )
    result = llm.predict(final_prompt)
   
    st.write("결과:")
    st.write(result)

