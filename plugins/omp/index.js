import { communicationStylePrompt, hasCommunicationStyle } from '../shared/bootstrap.js';

export default function clarity(api) {
  api.on('before_agent_start', ({ systemPrompt }) => {
    if (systemPrompt.some(hasCommunicationStyle)) return;
    return { systemPrompt: [...systemPrompt, communicationStylePrompt] };
  });
}
