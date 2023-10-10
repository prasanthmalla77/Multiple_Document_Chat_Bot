css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 100px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://uploads-ssl.webflow.com/5ec00594cbeb6ee5810ae410/600b35620d8600c3d19c0fd5_Drishya%20Logo%20-%20White-p-500.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ea4baa0b-151d-4b03-8661-d65d23cab2c2/d4o017u-cd28dfde-3b07-4e44-a09e-a02f7d43692b.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTpmaWxlLmRvd25sb2FkIl0sIm9iaiI6W1t7InBhdGgiOiIvZi9lYTRiYWEwYi0xNTFkLTRiMDMtODY2MS1kNjVkMjNjYWIyYzIvZDRvMDE3dS1jZDI4ZGZkZS0zYjA3LTRlNDQtYTA5ZS1hMDJmN2Q0MzY5MmIucG5nIn1dXX0.P3JQ5f2nl8Q9oWlqcqc8e9GHLEVmQZWm9OnwhWGR5vk">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
