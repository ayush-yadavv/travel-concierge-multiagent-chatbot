import { DialogflowMessenger } from '@/components/dialogflow-messenger'

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-r from-blue-50 to-indigo-50 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-gray-900 mb-6">
          Welcome to Travel Concierge
        </h1>
        <p className="text-lg text-gray-700 mb-4">
          Your personal travel assistant is ready to help! Click the chat bubble in the bottom right corner to:
        </p>
        <ul className="list-disc list-inside text-gray-700 space-y-2 ml-4">
          <li>Plan your next trip</li>
          <li>Get travel recommendations</li>
          <li>Find the best destinations</li>
          <li>Answer your travel questions</li>
        </ul>
      </div>
      <DialogflowMessenger />
    </main>
  )
}