import { communicationStylePrompt, hasCommunicationStyle } from '../shared/bootstrap.js';

export const ClarityPlugin = async () => ({
  'experimental.chat.system.transform': async (_input, output) => {
    if (!output.system.some(hasCommunicationStyle)) {
      output.system.push(communicationStylePrompt);
    }
  },
});
