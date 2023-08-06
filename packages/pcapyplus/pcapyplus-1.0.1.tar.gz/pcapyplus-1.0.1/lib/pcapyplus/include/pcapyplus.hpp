/*
 * Copyright (C) 2021 Hewlett Packard Enterprise Development LP.
 * Copyright (C) 2014-2021 CORE Security Technologies
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */

#ifndef __PPP_H__
#define __PPP_H__


extern "C" {
    PyObject* PyInit__pcapyplus(void);
}

// exception object
extern PyObject* PcapError;

#endif // __PPP_H__
