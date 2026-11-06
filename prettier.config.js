import { defineConfig } from '@archoleat/prettier-define-config';

export default defineConfig({
  overrides: [
    {
      files: ['*.mdc'],
      options: { parser: 'markdown' },
    },
    {
      files: ['*.js', '*.ts', '*.yaml'],
      options: {
        singleQuote: true,
      },
    },
  ],
});
