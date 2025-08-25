import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid, GridOptionsBuilder
from actors.service import ActorService


def clean_for_aggrid(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converte tudo que não for string, número ou boolean em string,
    para evitar problemas de serialização no AgGrid.
    """
    for col in df.columns:
        if not pd.api.types.is_numeric_dtype(df[col]) and not pd.api.types.is_bool_dtype(df[col]):
            df[col] = df[col].apply(lambda x: str(x) if not pd.isnull(x) else '')
    return df


def show_actors():
    actor_service = ActorService()
    st.title('Atores/Atrizes')

    # --- Formulário de cadastro ---
    st.subheader('Cadastrar Novo(a) Ator/Atriz')
    name = st.text_input('Nome')
    birthday = st.date_input(
        label='Data de Nascimento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    nationality_dropdown = ['BRAZIL', 'USA']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown,
    )
    if st.button('Cadastrar', key='btn_add_actor'):
        if name.strip() == "":
            st.error("O nome não pode ficar vazio!")
        else:
            new_actor = actor_service.create_actor(
                name=name,
                birthday=birthday,
                nationality=nationality,
            )
            if new_actor:
                st.success(f"Ator/Atriz '{name}' cadastrado(a) com sucesso!")
                st.session_state.actors = actor_service.get_actors()
                st.experimental_rerun()
            else:
                st.error('Erro ao cadastrar o(a) Ator/Atriz. Verifique os campos')

    # --- Lista de atores ---
    if 'actors' not in st.session_state:
        st.session_state.actors = actor_service.get_actors()
    actors = st.session_state.actors

    if actors:
        st.write('Lista de Atores/Atrizes:')
        actors_df = pd.json_normalize(actors)
        actors_df = clean_for_aggrid(actors_df)

        gb = GridOptionsBuilder.from_dataframe(actors_df)
        gb.configure_default_column(editable=False, sortable=True, filter=True, resizable=True)
        gb.configure_selection('single')
        gridOptions = gb.build()

        grid_response = AgGrid(
            actors_df,
            gridOptions=gridOptions,
            enable_enterprise_modules=False,
            key='actors_grid',
        )

        selected = grid_response.get('selected_rows', [])
        if selected:
            selected_actor = selected[0]
            st.subheader(f"Editar Ator/Atriz: {selected_actor['name']}")
            new_name = st.text_input('Novo nome', value=selected_actor['name'], key='edit_actor_name')
            # Adicione campos para editar birthday/nationality se desejar
            if st.button('Salvar edição', key='btn_edit_actor'):
                # Implemente aqui a chamada para editar o ator via service/repository se disponível
                st.success(f"Ator/Atriz atualizado(a) para '{new_name}'")
                st.session_state.actors = actor_service.get_actors()
                st.experimental_rerun()
    else:
        st.warning('Nenhum Ator/Atriz encontrado.')