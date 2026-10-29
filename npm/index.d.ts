export type Lang = 'en' | 'ja' | 'zh' | 'es' | 'pt' | 'de';
export type Category = 'effects' | 'aesthetics' | 'text_styles' | 'scenes' | 'occasions';

export interface Example {
  /** The work's page on fontvibe.ai. */
  url: string;
  /** Hotlinked image on FontVibe's CDN. */
  image: string;
}

export interface TestResult {
  /** General image model the standalone prompt was tested on, e.g. "gemini-2.5-flash-image". */
  model: string;
  /** ISO date of the test. */
  date: string;
  /** The words used in place of {{TEXT}}. */
  text: string;
  /** URL of the test render, or "" while it is not hosted. */
  image: string;
  image_file: string;
  passed: true;
  note: string;
}

export interface Style {
  /** FontVibe style id, e.g. "neon_glow". */
  id: string;
  /** URL slug, e.g. "neon-glow". */
  slug: string;
  category: Category;
  /** Parent style id for sub-styles, "" for top-level styles. */
  parent: string;
  tags: string[];
  /** FontVibe's own names; "" where no translation is published. */
  names: Record<Lang, string>;
  /** FontVibe's own descriptions; "" where no translation is published. */
  description: Record<Lang, string>;
  /** https://fontvibe.ai/styles/<slug> */
  fontvibe_url: string;
  preview_image: string;
  examples: Example[];
  /** Standalone prompt with a {{TEXT}} placeholder. */
  prompt: string;
  /** FontVibe's original style layer (needs FontVibe's font pipeline; not a complete prompt). */
  style_layer: { core: string; scene: string };
  test: TestResult;
  /** True when FontVibe changed the style after this prompt was written. */
  stale: boolean;
  /** Path of the Markdown page in the repository. */
  file: string;
}

export interface Stats {
  styles_on_fontvibe: number;
  excluded_trademark: number;
  candidates: number;
  published: number;
  failed_test: number;
  untested: number;
  no_prompt: number;
  by_category: Record<Category, number>;
  languages: Lang[];
  missing_translations: Record<Lang, { names: number; description: number }>;
  stale: number;
  test_model: string[];
}

export const LANGS: Lang[];
export const PLACEHOLDER: '{{TEXT}}';
export const stats: Stats;
export function all(): Style[];
export function get(idOrSlug: string): Style | undefined;
export function list(opts?: { category?: string; tag?: string; limit?: number }): Style[];
export function search(query: string, opts?: { lang?: Lang; category?: string; limit?: number }): Style[];
export function prompt(idOrSlug: string, text: string): string;
export function name(idOrSlug: string, lang?: Lang): string | undefined;
export function categories(): Category[];
export function tags(): { tag: string; count: number }[];
export function attribution(idOrSlug?: string, format?: 'markdown' | 'html' | 'text'): string;

declare const _default: {
  LANGS: typeof LANGS; PLACEHOLDER: typeof PLACEHOLDER; stats: Stats;
  all: typeof all; get: typeof get; list: typeof list; search: typeof search; prompt: typeof prompt;
  name: typeof name; categories: typeof categories; tags: typeof tags; attribution: typeof attribution;
};
export default _default;
