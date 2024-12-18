'use client'

import { useEffect } from 'react'
import Script from 'next/script'

export function DialogflowMessenger() {
  useEffect(() => {
    const createMessenger = () => {
      const messenger = document.createElement('df-messenger')
      messenger.setAttribute('location', 'us-central1')
      messenger.setAttribute('project-id', 'ai-hospital-agents-9696')
      messenger.setAttribute('agent-id', '93cd472e-561a-422c-b57d-7f0241eed9e6')
      messenger.setAttribute('language-code', 'en')
      messenger.setAttribute('max-query-length', '-1')

      const chatBubble = document.createElement('df-messenger-chat-bubble')
      chatBubble.setAttribute('chat-title', 'Travel Concierge Bot')
      
      messenger.appendChild(chatBubble)
      document.body.appendChild(messenger)
    }

    if (!document.querySelector('df-messenger')) {
      createMessenger()
    }
  }, [])

  return (
    <>
      <link 
        rel="stylesheet" 
        href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css" 
      />
      <Script 
        src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"
        onLoad={() => {
          console.log('Dialogflow Messenger script loaded')
        }}
      />
    </>
  )
}