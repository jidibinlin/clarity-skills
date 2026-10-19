export const communicationStylePrompt = __CLARITY_COMMUNICATION_STYLE__;
const communicationStyleTag = __CLARITY_COMMUNICATION_STYLE_TAG__;

export function hasCommunicationStyle(text) {
  const start = text.indexOf(communicationStyleTag);
  return start !== -1 && text.indexOf('</clarity-communication-style>', start + communicationStyleTag.length) !== -1;
}
