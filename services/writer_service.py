
class Writer:
    def human_msg(message: str) -> str:
        return f'''
            <div style="display: flex; align-items: center; justify-content: flex-end; margin-bottom: 10px;">
                <div style="background-color: #dcf8c6; border-radius: 10px; padding: 10px; max-width: 60%;">
                    {message}
                </div>
                <span style="margin-left: 10px;">👤</span>
            </div>
            '''

    def ai_msg(message: str) -> str:
        return f'''
            <div style="display: flex; align-items: center; justify-content: flex-start; margin-bottom: 10px;">
                <span style="margin-right: 10px;">🤖</span>
                <div style="background-color: #f1f0f0; border-radius: 10px; padding: 10px; max-width: 60%;">
                    {message}
                </div>
            </div>
        '''