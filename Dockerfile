FROM eosineye1/sam:1
WORKDIR /app
RUN pip3 install streamlit
RUN python -m pip install -U matplotlib
RUN pip3 install Image
RUN pip3 install pandas
RUN pip3 install altair
COPY . .
CMD streamlit run app.py
